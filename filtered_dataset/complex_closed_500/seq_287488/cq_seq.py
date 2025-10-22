import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00095, 0.11879).threePointArc((-0.00483, 0.12213), (-0.01149, 0.12167)).lineTo(-0.02798, 0.11535).lineTo(-0.02798, 0.127).lineTo(0.00687, 0.127).lineTo(0.00687, 0.11245).lineTo(0.00095, 0.11879).close()
solid=wp_sketch0.add(loop0).extrude(-0.07703699290685613)
