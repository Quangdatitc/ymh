pushd z:自動分析
rd 起動用bat /s /q
pushd C:\Program Files\KNIME
knime.exe --launcher.suppressErrors -nosave -nosplash -reset -consoleLog -application org.knime.product.KNIME_BATCH_APPLICATION -workflowFile="\\133.215.136.79\i_情シス\自動分析\管理用\自動化用Bat自動作成.knwf"
knime.exe --launcher.suppressErrors -nosave -nosplash -reset -consoleLog -application org.knime.product.KNIME_BATCH_APPLICATION -workflowFile="\\133.215.136.79\i_情シス\自動分析\管理用\タスクスケジューラ更新.knwf"