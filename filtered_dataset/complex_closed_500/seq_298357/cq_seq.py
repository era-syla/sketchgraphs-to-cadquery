import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00663, 0.00635).lineTo(-0.00607, 0.00635).lineTo(-0.00607, -0.00635).lineTo(0.00663, -0.00635).lineTo(0.00663, 0.00635).close()
solid=wp_sketch0.add(loop0).extrude(-0.01732246175354488)
