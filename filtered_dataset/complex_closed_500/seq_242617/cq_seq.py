import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02861, 0.01589).lineTo(0.11109, 0.01589).lineTo(0.11109, 0.01214).lineTo(-0.02861, 0.01214).lineTo(-0.02861, 0.01589).close()
solid=wp_sketch0.add(loop0).extrude(-0.2861031611426385)
