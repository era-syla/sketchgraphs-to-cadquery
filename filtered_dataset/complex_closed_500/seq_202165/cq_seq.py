import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00319, 0.03587).lineTo(0.04761, 0.03587).lineTo(0.04761, -0.01493).lineTo(-0.00319, -0.01493).lineTo(-0.00319, 0.03587).close()
solid=wp_sketch0.add(loop0).extrude(-0.014220978831661311)
