#!/bin/sh


while getopts ":m:" mode; do
  case $mode in
    m)
      case $OPTARG in
        --update)
            sudo chown -R 1000:1000 ./.docker
            docker-compose down -v
            docker-compose up -d --build
          ;;
        *)
          echo "Invalid option: -$OPTARG" >&2
          exit 1
          ;;
      esac
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done