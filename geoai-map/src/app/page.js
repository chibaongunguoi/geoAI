"use client";
import Image from "next/image";
import styles from "./page.module.css";
import dynamic from "next/dynamic";

const MapView = dynamic(() => import("./components/MapView"), {
  ssr: false,
});

export default function Home() {
  return (
    <MapView />
  );
}
