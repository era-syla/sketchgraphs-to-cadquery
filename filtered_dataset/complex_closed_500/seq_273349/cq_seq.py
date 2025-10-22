import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0762, 0.0127).lineTo(-0.0762, -0.0127).lineTo(-0.0635, -0.0127).threePointArc((-0.0508, 0.0), (-0.0635, 0.0127)).lineTo(-0.0762, 0.0127).close()
solid=wp_sketch0.add(loop0).extrude(0.06120494642355805)
