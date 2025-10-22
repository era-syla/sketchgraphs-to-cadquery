import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00368, -0.04245).threePointArc((0.0381, -0.01486), (-0.00368, 0.01273)).lineTo(-0.00368, -0.04245).close()
solid=wp_sketch0.add(loop0).extrude(0.08546064569026851)
