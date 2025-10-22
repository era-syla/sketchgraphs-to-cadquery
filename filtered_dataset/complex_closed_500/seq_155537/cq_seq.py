import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.382, -0.167).lineTo(0.382, -0.167).lineTo(0.382, -0.267).lineTo(-0.382, -0.267).lineTo(-0.382, -0.167).close()
solid=wp_sketch0.add(loop0).extrude(0.8602023139274374)
