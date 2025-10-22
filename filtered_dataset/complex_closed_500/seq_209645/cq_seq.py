import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.10541, 0.04648).lineTo(-0.09979, 0.04648).lineTo(-0.09979, 0.0).lineTo(-0.07131, -0.03731).lineTo(-0.07529, -0.04068).lineTo(-0.10541, -0.00514).lineTo(-0.10541, 0.04648).close()
solid=wp_sketch0.add(loop0).extrude(-0.2514418345315011)
