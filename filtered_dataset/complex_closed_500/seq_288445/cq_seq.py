import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.13737, 1.18713).lineTo(0.14198, 1.16215).lineTo(0.1451, 1.16273).lineTo(0.14049, 1.1877).lineTo(0.13737, 1.18713).close()
solid=wp_sketch0.add(loop0).extrude(0.06763334715587073)
