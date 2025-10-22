import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0084, -0.0035).threePointArc((-0.008, -0.0031), (-0.0076, -0.0035)).lineTo(-0.0076, -0.0185).threePointArc((-0.008, -0.0189), (-0.0084, -0.0185)).lineTo(-0.0084, -0.0035).close()
solid=wp_sketch0.add(loop0).extrude(0.010025019316927754)
