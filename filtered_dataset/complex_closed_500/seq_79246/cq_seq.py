import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.67345, 0.38574).lineTo(-0.81315, 0.38574).lineTo(-0.81315, 0.24604).lineTo(-0.67345, 0.38574).close()
solid=wp_sketch0.add(loop0).extrude(-0.356971284865539)
