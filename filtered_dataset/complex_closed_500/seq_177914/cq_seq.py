import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.025, 0.0).lineTo(0.025, 1.3).lineTo(-0.0, 1.3).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-2.852010771835487)
