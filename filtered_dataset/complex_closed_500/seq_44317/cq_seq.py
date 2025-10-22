import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.03358, -0.03145).lineTo(0.03273, -0.03061).lineTo(0.03059, -0.03271).lineTo(0.03146, -0.03358).lineTo(0.03358, -0.03145).close()
solid=wp_sketch0.add(loop0).extrude(-0.005111408105148139)
