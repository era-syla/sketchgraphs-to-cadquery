import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0889, -0.02858).lineTo(0.02524, -0.02858).lineTo(0.02524, -0.02223).threePointArc((0.03635, -0.01111), (0.02524, -0.0)).lineTo(-0.0889, 0.0).lineTo(-0.0889, -0.02858).close()
solid=wp_sketch0.add(loop0).extrude(0.2712570462422554)
