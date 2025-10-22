import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.08409, -0.08149).lineTo(0.07808, -0.08149).lineTo(0.07808, 0.08019).lineTo(-0.08409, 0.08019).lineTo(-0.08409, -0.08149).close()
solid=wp_sketch0.add(loop0).extrude(0.45017068978418884)
