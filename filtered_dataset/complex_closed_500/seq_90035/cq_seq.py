import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.03175, 0.0).lineTo(0.03175, 0.1143).lineTo(0.0, 0.1143).lineTo(0.35878, 0.1143).lineTo(0.35878, 0.0).lineTo(0.03175, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.7823196723059779)
