import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04461, 0.01729).lineTo(-0.03929, 0.01383).lineTo(-0.00332, 0.06922).lineTo(-0.00864, 0.07268).lineTo(-0.04461, 0.01729).close()
solid=wp_sketch0.add(loop0).extrude(0.011088033234436035)
