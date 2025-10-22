import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.30117, 0.01459).lineTo(-0.28017, 0.01459).threePointArc((-0.27947, 0.0143), (-0.27917, 0.01359)).lineTo(-0.27917, 0.00809).threePointArc((-0.27947, 0.00738), (-0.28017, 0.00709)).lineTo(-0.30117, 0.00709).threePointArc((-0.30188, 0.00738), (-0.30217, 0.00809)).lineTo(-0.30217, 0.01359).threePointArc((-0.30188, 0.0143), (-0.30117, 0.01459)).close()
solid=wp_sketch0.add(loop0).extrude(0.04468234455547448)
