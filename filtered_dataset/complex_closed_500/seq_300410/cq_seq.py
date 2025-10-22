import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.025, 0.005).lineTo(0.1, 0.005).lineTo(0.1, 0.055).lineTo(0.025, 0.055).lineTo(0.025, 0.005).close()
solid=wp_sketch0.add(loop0).extrude(-0.15282351391329066)
