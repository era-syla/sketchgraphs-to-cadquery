import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04387, -0.08381).lineTo(-0.13587, -0.08381).lineTo(-0.13587, 0.06519).lineTo(-0.04387, 0.06519).lineTo(-0.04387, -0.08381).close()
solid=wp_sketch0.add(loop0).extrude(-0.3348975590517227)
