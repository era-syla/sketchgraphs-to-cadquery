import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.02927, 0.0).lineTo(0.0, 0.0).lineTo(0.02547, 0.02686).lineTo(0.02927, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.02056390609769667)
