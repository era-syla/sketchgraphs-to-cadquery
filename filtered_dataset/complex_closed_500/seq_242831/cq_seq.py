import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.17691, -0.02136).lineTo(0.16532, -0.02136).lineTo(0.16532, 0.01066).lineTo(0.17691, 0.01066).lineTo(0.17691, -0.02136).close()
solid=wp_sketch0.add(loop0).extrude(0.01583121672930248)
