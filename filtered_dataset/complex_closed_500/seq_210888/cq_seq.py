import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.05451, 0.01023).lineTo(0.08695, 0.01023).lineTo(0.08695, -0.01082).lineTo(0.05451, -0.01082).lineTo(0.05451, 0.01023).close()
solid=wp_sketch0.add(loop0).extrude(0.06947892413112297)
