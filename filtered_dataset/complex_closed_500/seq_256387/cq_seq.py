import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.27097, 0.05226).lineTo(0.26797, 0.05226).lineTo(0.26797, 0.0203).lineTo(0.27097, 0.0203).lineTo(0.27097, 0.05226).close()
solid=wp_sketch0.add(loop0).extrude(-0.060332627065776814)
