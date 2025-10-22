import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.84125).lineTo(-0.21641, 0.84125).lineTo(-0.21641, 3.02971).lineTo(-0.0, 3.02971).lineTo(0.0, 0.84125).close()
solid=wp_sketch0.add(loop0).extrude(-4.674155773228525)
