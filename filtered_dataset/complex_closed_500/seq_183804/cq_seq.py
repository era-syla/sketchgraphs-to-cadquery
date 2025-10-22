import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.006, -0.00411).lineTo(-0.006, -0.00411).lineTo(-0.006, 0.00411).lineTo(0.006, 0.00411).lineTo(0.006, -0.00411).close()
solid=wp_sketch0.add(loop0).extrude(-0.02112555910392148)
