import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.02763, 0.0347).lineTo(0.03095, 0.0347).lineTo(0.03095, 0.011).lineTo(0.02763, 0.011).lineTo(0.02763, 0.0347).close()
solid=wp_sketch0.add(loop0).extrude(0.023433207147527436)
