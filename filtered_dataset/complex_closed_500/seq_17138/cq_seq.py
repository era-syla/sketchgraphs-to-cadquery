import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.18141, 0.09421).lineTo(0.12339, 0.09421).lineTo(0.12339, -0.11534).lineTo(-0.18141, -0.11534).lineTo(-0.18141, 0.09421).close()
solid=wp_sketch0.add(loop0).extrude(-0.574043754020409)
