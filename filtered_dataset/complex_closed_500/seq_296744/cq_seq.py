import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0435, 0.02029).lineTo(0.04773, 0.01122).lineTo(0.0586, 0.01629).lineTo(0.05691, 0.01992).lineTo(0.06598, 0.02415).lineTo(0.06344, 0.02958).lineTo(0.0435, 0.02029).close()
solid=wp_sketch0.add(loop0).extrude(-0.02452430156195894)
