import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0425, -0.01485).lineTo(-0.0425, 0.00565).lineTo(-0.037, 0.00565).lineTo(-0.037, -0.01485).lineTo(-0.0425, -0.01485).close()
solid=wp_sketch0.add(loop0).extrude(0.023833828210546835)
