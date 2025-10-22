import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.09003, -0.08523).lineTo(0.08449, -0.08523).lineTo(0.08449, 0.08478).lineTo(-0.09003, 0.08478).lineTo(-0.09003, -0.08523).close()
solid=wp_sketch0.add(loop0).extrude(0.3459274092263632)
