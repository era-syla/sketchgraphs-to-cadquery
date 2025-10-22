import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01906, 0.03507).lineTo(0.02094, 0.03507).lineTo(0.02094, -0.00493).lineTo(-0.01906, -0.00493).lineTo(-0.01906, 0.03507).close()
solid=wp_sketch0.add(loop0).extrude(-0.09300519301093411)
