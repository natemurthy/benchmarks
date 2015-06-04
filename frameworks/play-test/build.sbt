import sbt._

name := """play-test"""

version := "0.1-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayScala)

scalaVersion in ThisBuild := "2.10.4"

scalacOptions ++= Seq(
  "-feature",
  "-language:postfixOps"
)

resolvers ++= Seq(
  "Sonatype Releases" at "https://oss.sonatype.org/content/repositories/releases/"
)

libraryDependencies ++= Seq(
  "com.github.tototoshi" %% "play-json4s-jackson" % "0.3.1"  withSources(),
  "org.json4s"           %% "json4s-jackson"      % "3.2.9"  withSources()
)
