#! /usr/bin/fish


function git_dir_status
  function sinh_gstatus
    set path $argv[1]
    set git_stats (git -C $path rev-parse 2>/dev/null)
    if git -C $path rev-parse --git-dir >/dev/null 2>&1
      set count (git -C $path status --porcelain | wc -l)
      if test "$count" -gt 0
        echo $path "|" $count 
      end
    else
      find $path -maxdepth 1 -mindepth 1 -type d| while read sub;
        sinh_gstatus $sub
      end
    end
  end

  /bin/cat ~/dir-to-watches | while read i;
    set repos_changed $repos_changed (sinh_gstatus $i)
  end

  set -f selected_path (
    for val in $repos_changed
      echo "$val"
    end | fzf \
       --query=(commandline --current-token)
  )

  if test $status -eq 0
    for line in $selected_path
      set -f path (string split --field 1 "|" $line)
    end
    commandline --current-token --replace (string join " " "cd" $path)
  end
end
