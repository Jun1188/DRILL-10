# DRILL-10 개발 기획 및 요구사항

## 현재 범위

- 현재 단계는 Python 및 pico2d 개발 환경 준비이다.
- DRILL-10 과제 요구사항, 마감 시각, 실행 코드와 이미지 목록은 아직 정해지지 않았다.
- 과제 안내를 받은 후 이 문서를 실제 구현과 일치하도록 갱신한다.

## 개발 환경

- Python: 3.13.15
- 인터프리터: `C:\Users\변준영\AppData\Local\Programs\Python\Python313\python.exe`
- pico2d: 1.5.1
- 기존 시스템 Python 환경을 사용한다.
- `.gitignore`는 `2DGP-2024184011`과 동일한 제외 규칙을 사용한다.
- 작성하거나 수정하는 텍스트 파일은 UTF-8 BOM으로 저장한다.

## 실행 방법

1. VS Code에서 `DRILL-10` 폴더를 연다.
2. `Python: Select Interpreter`에서 위 Python 3.13 경로를 선택한다.
3. 실행 코드를 작성한 후 해당 파일을 열고 `Python: Current File` 설정으로 F5를 실행한다.
4. 실행 작업 폴더는 해당 Python 파일이 있는 폴더이다.

필요한 패키지가 없는 환경에서는 아래 명령을 사용한다.

```powershell
& 'C:\Users\변준영\AppData\Local\Programs\Python\Python313\python.exe' -m pip install -r .\requirements.txt
```

## 사용자 확인 항목

빌드와 테스트는 사용자가 수행한다. 환경 준비 중에는 실행 확인을 수행하지 않았다.

- 위 Python 경로로 `import pico2d`가 성공하는지 확인한다.
- 실행 코드 작성 후 F5가 Python 3.13을 사용하는지 확인한다.
- 과제 구현 후 창 표시, 입력 처리 및 이미지 로딩 항목을 추가하고 확인한다.

## GitHub 및 제출 상태

- Git 저장소 초기화, 커밋 및 GitHub 게시를 아직 수행하지 않았다.
- 게시 시 DRILL-10 전용 Public 저장소를 사용한다.
- 실제 개발 과정에 따라 의미 있는 변경 단위로 커밋한다.
- 게시 시 PRD.md, 실행 코드, 필요한 이미지와 개발 커밋 기록을 원격에서 확인한다.
- `.vscode/`는 제외되므로 로컬 인터프리터와 디버그 설정은 게시되지 않는다.
- e-Class 제출은 아직 수행하지 않았다. 과제 안내에서 마감 시각과 제출 자료를 확인한다.
