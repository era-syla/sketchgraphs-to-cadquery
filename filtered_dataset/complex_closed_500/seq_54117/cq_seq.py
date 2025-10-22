import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.46514, -0.14796).lineTo(-0.44514, -0.14796).lineTo(-0.44514, -0.18796).lineTo(-0.46514, -0.18796).lineTo(-0.46514, -0.14796).close()
solid=wp_sketch0.add(loop0).extrude(-0.05862254577522504)
