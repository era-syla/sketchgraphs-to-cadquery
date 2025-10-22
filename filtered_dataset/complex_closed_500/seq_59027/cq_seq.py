import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00936, 0.04287).threePointArc((-0.0549, 0.05085), (-0.10102, 0.0539)).lineTo(-0.10102, -0.0097).lineTo(-0.00936, -0.0097).lineTo(-0.00936, 0.04287).close()
solid=wp_sketch0.add(loop0).extrude(-0.0631923888453713)
