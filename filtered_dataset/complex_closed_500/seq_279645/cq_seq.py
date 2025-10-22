import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01236, -0.02979).lineTo(-0.05736, -0.02979).lineTo(-0.05736, 0.00521).threePointArc((-0.02938, 0.01567), (-0.01236, 0.04021)).lineTo(-0.01236, -0.02979).close()
solid=wp_sketch0.add(loop0).extrude(-0.17224848181640337)
