import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04409, 0.0604).lineTo(0.00141, 0.0604).lineTo(0.00141, 0.0574).lineTo(-0.04409, 0.0574).lineTo(-0.04409, 0.0604).close()
solid=wp_sketch0.add(loop0).extrude(0.07682856208176184)
