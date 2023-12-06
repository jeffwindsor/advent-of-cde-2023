with import <nixpkgs> {};
let
  python-lsp = python311.withPackages(ps: with ps; [
    python-lsp-server
  ]);
    
in mkShell {
  packages = [
    python-lsp
  ];
}
