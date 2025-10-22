import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.08546, 0.0472).lineTo(-0.02554, 0.0472).lineTo(-0.02554, 0.02405).threePointArc((-0.027, 0.02051), (-0.03054, 0.01905)).lineTo(-0.08046, 0.01905).threePointArc((-0.084, 0.02051), (-0.08546, 0.02405)).lineTo(-0.08546, 0.0472).close()
solid=wp_sketch0.add(loop0).extrude(-0.053616477966477276)
