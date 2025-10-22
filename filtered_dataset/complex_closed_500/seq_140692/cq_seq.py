import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.01949).threePointArc((-0.01838, 0.02711), (-0.026, 0.04549)).lineTo(-0.041, 0.04549).lineTo(-0.055, -0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.013167361720082855)
