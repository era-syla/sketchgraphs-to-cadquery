import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(1.395, 0.225).lineTo(-1.395, 0.225).lineTo(-1.395, -0.225).lineTo(1.395, -0.225).lineTo(1.395, 0.225).close()
solid=wp_sketch0.add(loop0).extrude(2.0591013622300696)
