import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.014, -0.0105).lineTo(-0.014, -0.0105).lineTo(-0.014, 0.0105).lineTo(0.014, 0.0105).lineTo(0.014, -0.0105).close()
solid=wp_sketch0.add(loop0).extrude(-0.007535834372583356)
