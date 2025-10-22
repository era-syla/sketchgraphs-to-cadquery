import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.18178, 0.0254).lineTo(0.11828, 0.0254).lineTo(0.11828, 0.06985).lineTo(0.18178, 0.06985).lineTo(0.18178, 0.0254).close()
solid=wp_sketch0.add(loop0).extrude(0.0228189833079821)
