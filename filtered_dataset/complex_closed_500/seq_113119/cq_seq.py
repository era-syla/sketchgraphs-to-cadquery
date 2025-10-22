import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(4.2672, 14.5034).lineTo(5.1816, 14.5034).lineTo(5.1816, 11.9634).lineTo(5.3086, 11.9634).lineTo(5.3086, 14.6304).lineTo(4.2672, 14.6304).lineTo(4.2672, 14.5034).close()
solid=wp_sketch0.add(loop0).extrude(1.8762651778847914)
