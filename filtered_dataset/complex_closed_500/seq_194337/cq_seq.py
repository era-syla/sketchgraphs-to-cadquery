import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0245, 0.03225).lineTo(0.0245, 0.03225).lineTo(0.0245, -0.03225).lineTo(-0.0245, -0.03225).lineTo(-0.0245, 0.03225).close()
solid=wp_sketch0.add(loop0).extrude(-0.06241430337727091)
