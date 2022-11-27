modify pom.xml
```
<argLine> -XX:hashCode=1 -javaagent:${rvPath}/lib/rv-predict.jar="--base-log-dir ${real_world}/RV-Predict/zookeeper --log-dirname zookeeper" </argLine>
```