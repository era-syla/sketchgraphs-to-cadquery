import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.35, -0.2).lineTo(0.35, -0.268).lineTo(0.29, -0.268).lineTo(0.29, -0.2).lineTo(0.35, -0.2).close()
solid=wp_sketch0.add(loop0).extrude(-0.005669204610840041)
