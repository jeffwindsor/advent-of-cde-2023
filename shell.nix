with import <nixpkgs> {};
let
  python-advent = python311.withPackages(ps: with ps; [
      # advent-of-code-data
      # advent-of-code-ocr
      colorama
      numpy
      parse
      pytest
      rich
    ]);
    
in mkShell {
  packages = [
    python-advent
    entr
  ];
  
  # shellHook = ''
  #   echo "  █████╗  ██████╗  ██████╗██████╗  ██████╗ ██████╗ ██████╗ "
  #   echo " ██╔══██╗██╔═══██╗██╔════╝╚════██╗██╔═████╗╚════██╗╚════██╗"
  #   echo " ███████║██║   ██║██║      █████╔╝██║██╔██║ █████╔╝ █████╔╝"
  #   echo " ██╔══██║██║   ██║██║     ██╔═══╝ ████╔╝██║██╔═══╝  ╚═══██╗"
  #   echo " ██║  ██║╚██████╔╝╚██████╗███████╗╚██████╔╝███████╗██████╔╝"
  #   echo " ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚══════╝ ╚═════╝ ╚══════╝╚═════╝ "
  #   echo ""
  # '';
}
